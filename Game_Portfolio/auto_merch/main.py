"""
MAIN EXECUTION FLOW
Tích hợp tất cả tasks để thực hiện quy trình đăng ký Amazon Merch

Workflow:
1. Prepare Phase: Get user data → Buy mail
2. Log Phase: Write PENDING to Excel
3. Run Phase: Launch Camoufox (Anti-Detection) → Run automation
4. Finalize Phase: Update Excel to SUCCESS/FAILED
"""

import logging
import sys
import asyncio
from task2_data_manager import get_user_data
from task3_mail_service import buy_hotmail
from task4_camoufox_workflow import start_automation
from task5_excel_reporter import save_pending, update_success, update_failed, update_status
from proxy_config import generate_random_proxy

# ==================== LOGGING SETUP ====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('merch_automation.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# ==================== MAIN FUNCTION ====================
async def main():
    """
    Main execution flow (Async for Camoufox)
    """
    logger.info("\n" + "=" * 70)
    logger.info("🚀 BẮT ĐẦU QUY TRÌNH ĐĂNG KÝ AMAZON MERCH (CAMOUFOX)")
    logger.info("=" * 70)

    row_index = None

    try:
        # ==================== GIAI ĐOẠN 1: CHUẨN BỊ ====================
        logger.info("\n" + "=" * 70)
        logger.info("📋 GIAI ĐOẠN 1: CHUẨN BỊ DỮ LIỆU")
        logger.info("=" * 70)

        # Task 2: Lấy user data
        logger.info("\n🔹 Task 2: Lấy user data...")
        user_data = get_user_data()

        if not user_data:
            logger.error("❌ Không lấy được user data!")
            return False

        # Task 3: Mua mail
        logger.info("\n🔹 Task 3: Mua mail...")
        mail_data = buy_hotmail()

        if not mail_data:
            logger.error("❌ Không mua được mail!")
            return False

        logger.info("\n✅ Giai đoạn 1 hoàn tất!")
        logger.info(f"   Email: {mail_data['mail']}")
        logger.info(f"   Fullname: {user_data['fullname']}")

        # ==================== GIAI ĐOẠN 2: LƯU VẾT ====================
        logger.info("\n" + "=" * 70)
        logger.info("📝 GIAI ĐOẠN 2: GHI TRẠNG THÁI PENDING")
        logger.info("=" * 70)

        # Task 6: Ghi PENDING (profile_name = "Camoufox")
        row_index = save_pending(mail_data, user_data, "Camoufox")

        if not row_index:
            logger.error("❌ Không ghi được PENDING vào Excel!")
            return False

        logger.info("\n✅ Giai đoạn 2 hoàn tất!")

        # ==================== GIAI ĐOẠN 3: THỰC THI ====================
        logger.info("\n" + "=" * 70)
        logger.info("🚀 GIAI ĐOẠN 3: THỰC THI AUTOMATION (CAMOUFOX)")
        logger.info("=" * 70)

        # Generate random proxy
        logger.info("\n🔹 Generate random proxy...")
        proxy_config = generate_random_proxy()

        # Task 4 + 5: Chạy Camoufox automation
        logger.info("\n🔹 Task 4+5: Khởi chạy Camoufox và chạy automation...")
        result = await start_automation(
            user_data=user_data,
            mail_data=mail_data,
            headless=False,  # ⚠️ Đổi thành True để chạy ẩn (KHÔNG khuyến nghị)
            proxy_config=proxy_config  # ✅ Sử dụng proxy
        )

        if not result:
            logger.error("❌ Automation thất bại!")
            raise Exception("Camoufox automation failed")

        # Xử lý result (dict với success, status, message)
        if result.get('success'):
            # Hoàn tất toàn bộ => SUCCESS
            logger.info("\n✅ Giai đoạn 3 hoàn tất!")
            logger.info("\n" + "=" * 70)
            logger.info("✅ GIAI ĐOẠN 4: CẬP NHẬT SUCCESS")
            logger.info("=" * 70)
            update_success(row_index)
        else:
            # Có status khác (require_phone, error, etc.)
            status = result.get('status', 'error')
            message = result.get('message', result.get('error', ''))
            logger.warning(f"⚠️ Automation dừng với status: {status}")
            update_status(row_index, status, message)
            return False

        logger.info("\n" + "=" * 70)
        logger.info("🎉 HOÀN THÀNH TOÀN BỘ QUY TRÌNH!")
        logger.info("=" * 70)

        return True

    except Exception as e:
        logger.error(f"\n❌ LỖI: {e}")
        import traceback
        traceback.print_exc()

        # Cập nhật FAILED nếu đã ghi PENDING
        if row_index:
            update_failed(row_index, str(e))

        return False

# ==================== ENTRY POINT ====================
if __name__ == "__main__":
    success = asyncio.run(main())

    if success:
        logger.info("\n✅ Script kết thúc thành công!")
        sys.exit(0)
    else:
        logger.error("\n❌ Script kết thúc với lỗi!")
        sys.exit(1)

