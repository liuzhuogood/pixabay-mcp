from fastmcp import FastMCP
import requests
from pydantic import Field
from pydantic.fields import FieldInfo
import logging
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
import argparse

# 解析命令行参数
def parse_arguments():
    parser = argparse.ArgumentParser(description='Pixabay MCP Server')
    parser.add_argument('--api-key', dest='pixabay_api_key', help='Pixabay API Key')
    return parser.parse_args()

# 处理命令行参数并设置环境变量
args = parse_arguments()
if args.pixabay_api_key:
    os.environ["PIXABAY_API_KEY"] = args.pixabay_api_key
    print(f"Pixabay API Key set from command line argument")

# Load environment variables
load_dotenv()

# Configure logging
# log_dir = os.path.dirname(__file__)
# log_file = os.path.join(log_dir, f"app_{datetime.now().strftime('%Y%m%d')}.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        # logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("pixabay-mcp")

# Create an MCP server
mcp = FastMCP("Image Search", dependencies=["requests", "pydantic", "python-dotenv"])


@mcp.tool()
def search_image(q: str = Field(..., description="搜索关键词"),
                 lang: str = Field("zh", description="语言"),
                 image_type: str = Field("photo", description="图片类型,Accepted values: photo, illustration, vector"),
                 category: str = Field("all",
                                       description="分类,Accepted values: backgrounds, fashion, nature, science, education, feelings, health, people, religion, places, animals, industry, computer, food, sports, transportation, travel, buildings, business, music"),

                 ) -> str:
    """ 根据关键词搜索图片,返回图片 URL 列表 """
    logger.info(f"Searching images with query: {q}, lang: {lang}, image_type: {image_type}, category: {category}")

    if isinstance(lang, FieldInfo):
        lang = lang.default
    if isinstance(image_type, FieldInfo):
        image_type = image_type.default
    if isinstance(category, FieldInfo):
        category = category.default

    # Get API key from environment variable
    api_key = os.getenv("PIXABAY_API_KEY")
    if not api_key:
        logger.error("PIXABAY_API_KEY not found in environment variables")
        return f"Error: PIXABAY_API_KEY not found in environment variables"

    url = f"https://pixabay.com/api/?key={api_key}&q={q}&image_type={image_type}&lang={lang}&category={category}&pretty=true"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        images = []
        if data and data["hits"]:
            images = [hit["largeImageURL"] for hit in data["hits"]]
            logger.info(f"Found {len(images)} images for query: {q}")
        else:
            logger.warning(f"No images found for query: {q}")
        return '\n'.join(images)
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error: {e}")
        return f"Error: {e}"
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return f"Error: {e}"


def main():
    logger.info("Starting Pixabay MCP server")
    mcp.run()


if __name__ == "__main__":
    # print(search_image(q="girl"))
    main()
