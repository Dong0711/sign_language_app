import mysql.connector
class database:
    def __init__(self) -> None:
        self.connection_string={
            'host': 'localhost',
    'user': 'root',
    'password': '0711',
    'database': 'sign_language'
        }
        pass
    def execute_non_query(self,query):
        try:
            db = mysql.connector.connect(**self.connection_string)
            cursor = db.cursor()
            cursor.execute(query)
            # Thực hiện câu truy vấn
            db.commit()
            print("successful")
            # Đóng kết nối CSDL
            db.close()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return
    
    def execute_query(self,query):
        record=None
        try:
            # Kết nối cơ sở dữ liệu thông qua chuỗi kết nối
            db = mysql.connector.connect(**self.connection_string)
            # Tạo con trỏ để thực hiện truy vấn
            cursor = db.cursor()
            # Thực thi câu lệnh SQL (câu lệnh query)
            cursor.execute(query)
            # Lấy tất cả các liệu nhận được và ghi vào biến
            record = cursor.fetchall()
        # kiểm tra nếu xảy ra lỗi kết nối CSDL
        except mysql.connector.errors as error:
            print("error", error)
            return
        # thực hiện viêc đóng CDL và con trỏ cũng như trả về giá trị sau khi thực hiện thành công
        finally:
            if db.is_connected():
                db.close()
                cursor.close()
                # print(record)
                return record       
# data=database()
# print(data.execute_query('select * from sign_dictionary'))