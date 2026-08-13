# ĐỀ BÀI: Xây dựng hệ thống đồng bộ dữ liệu đa nền tảng đám mây
# 1. Bối cảnh (Scenario)
# Công ty phần mềm của bạn đang phát triển một công cụ quản lý tệp tin cho phép người dùng đồng bộ hóa dữ liệu lên nhiều dịch vụ lưu trữ đám mây khác nhau. Hiện tại, hệ thống cần hỗ trợ hai nền tảng chính là Amazon S3 và Microsoft OneDrive. Trong tương lai, công ty có kế hoạch mở rộng thêm nhiều nền tảng khác.

# Bạn được giao nhiệm vụ thiết kế bộ khung (framework) cho tính năng đồng bộ này bằng Python, đảm bảo hệ thống dễ dàng mở rộng mà không phải sửa đổi code cốt lõi.

from abc import ABC, abstractmethod
# abc (Abstract Base Classes): Đây là một thư viện có sẵn của Python giúp tạo ra các lớp trừu tượng
# ABC: Helper class that provides a standard way to create an ABC using inheritance.
class CloudStorage(ABC):
  @abstractmethod
  def authenticate(self):
    pass
  @abstractmethod
  def upload_file(self, file_path):
    pass
  # @abstractmethod là Decorator đánh dấu các phương thức authenticate và upload_file là phương thức trừu tượng

class AWS_S3(CloudStorage):
  def authenticate(self):
    print("Đang xác thực với AWS IAM bằng Access Key...")
  def upload_file(self, file_path):
    print(f"Đang băm dữ liệu và tải {file_path} lên S3 Bucket...")
class GoogleDrive(CloudStorage):
  def authenticate(self):
    print("Đang xác thực qua OAuth 2.0 của Google...")
  def upload_file(self, file_path):
    print(f"Đang tạo thư mục và tải {file_path} lên Google Drive...")

class AppManager:
    def __init__(self, storage: CloudStorage):
        self.storage = storage # Dependency Injection
        
    def backup_data(self, file_path):
        self.storage.authenticate()
        self.storage.upload_file(file_path)
        print("Hoàn tất sao lưu!\n")

aws = AWS_S3()
app_aws = AppManager(aws)
app_aws.backup_data("/data/db_backup.sql")
