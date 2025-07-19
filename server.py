import logging, io, pyautogui, pygetwindow as gw, win32gui, win32con, win32com.client
from mcp.server.fastmcp import FastMCP, Image

logging.basicConfig(level=logging.INFO)
mcp = FastMCP("TradingViewTool")


@mcp.tool()
def open_tv() -> str:
    try:
        pyautogui.hotkey("ctrl", "alt", "t")
        pyautogui.sleep(5)
        logging.info("TradingView opened")
        win = pyautogui.getActiveWindow()
        win.minimize()
        return "Success"
    except Exception as e:
        logging.error(e)
        return f"Error: {e}"

@mcp.tool()
def get_chart_image() -> Image:
    try:
        pyautogui.hotkey("ctrl", "alt", "t")
        pyautogui.sleep(3)
        buf = io.BytesIO()
        img = pyautogui.screenshot()
        img.save(buf, format="PNG")
        win = pyautogui.getActiveWindow()
        win.minimize()
        return Image(data=buf.getvalue(), format="png")
    except Exception as e:
        logging.error(e)
        raise RuntimeError(f"Could not capture chart: {e}")

if __name__ == "__main__":
    mcp.run()
