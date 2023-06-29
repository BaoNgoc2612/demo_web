
from flask import Flask, render_template,request 
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://BaoNgoc:26122004@127.0.0.1:5433/BookShop'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


#Chọn tính năng
@app.route("/select")
def select():
    return render_template("select.html")


#Thêm khách hàng
@app.route("/addNewCustomer")
def addNewCustomer():
    return render_template("insert_new_customer.html")


@app.route("/addNewCustomerCommit")
def addNewCustomerCommit():
    customer_id = request.args.get("customer_id")
    customer_name = request.args.get("customer_name")
    address = request.args.get("address")
    phone = request.args.get("phone")
    email = request.args.get("email")
    customer = Customer(customer_id=customer_id, customer_name=customer_name, address=address, phone=phone, email=email)
    db.session.add(customer)
    db.session.commit()
    return render_template("insert_new_customer_success.html")


#Thêm thông tin nhân viên
@app.route("/addNewEmployee")
def addNewEmployee():
    return render_template("insert_new_employee.html")


@app.route("/addNewEmployeeCommit")
def addNewEmployeeCommit():
    employee_id = request.args.get("employee_id")
    employee_name = request.args.get("employee_name")
    gender = request.args.get("gender")
    birthday = request.args.get("birthday")
    phone = request.args.get("phone")
    email = request.args.get("email")
    address = request.args.get("address")
    position = request.args.get("position")
    salary = request.args.get("salary")
    employee = Employee(employee_id=employee_id, employee_name=employee_name, gender=gender, birthday=birthday, phone=phone, email=email, address=address, salary=salary, position=position)
    db.session.add(employee)
    db.session.commit()
    return render_template("insert_new_employee_success.html")


#Thêm thông tin kệ sách
@app.route("/addNewBookShelf")
def addNewBookShelf():
    return render_template("insert_new_book_shelf.html")


@app.route("/addNewBookShelfCommit")
def addNewBookShelfCommit():
    number = request.args.get("number")
    location = request.args.get("location")
    book_shelf = Book_Shelf(number=number, location=location)
    db.session.add(book_shelf)
    db.session.commit()
    return render_template("insert_new_book_shelf_success.html")


#Thêm thông tin thể loại sách
@app.route("/add_New_Kind_of_book")
def add_New_Kind_of_book():
    return render_template("insert_new_Kind_of_book.html")


@app.route("/add_new_Kind_of_bookCommit")
def add_new_Kind_of_bookCommit():
    id = request.args.get("id")
    name = request.args.get("name")
    book_shelf_number = request.args.get("book_shelf_number")
    kind_of_book = Kind_of_Book(id=id, name=name, book_shelf_number=book_shelf_number)
    db.session.add(kind_of_book)
    db.session.commit()
    return render_template("insert_new_kind_of_book_success.html")


#Thêm thông tin sách
@app.route("/addNewBook")
def addNewBook():
    return render_template("insert_new_book.html")


@app.route("/addNewBookCommit")
def addNewBookCommit():
    book_id = request.args.get("book_id")
    book_name = request.args.get("book_name")
    authors = request.args.get("authors")
    publishing_year = request.args.get("publishing_year")
    kind_of_book = request.args.get("kind_of_book")
    cost = request.args.get("cost")
    quantity = request.args.get("quantity")
    book = Book(book_id=book_id, book_name=book_name, authors=authors, publishing_year=publishing_year, kind_of_book=kind_of_book, cost=cost, quantity=quantity)
    db.session.add(book)
    db.session.commit()
    return render_template("insert_new_book_success.html")


#Thêm thông tin hóa đơn
@app.route("/addNewInvoice")
def addNewInvoice():
    return render_template("insert_new_invoice.html")


@app.route("/addNewInvoiceCommit")
def addNewInvoiceCommit():
    invoice_id = request.args.get("invoice_id")
    customer_id = request.args.get("customer_id")
    employee_id = request.args.get("employee_id")
    date_of_invoice = request.args.get("date_of_invoice")
    total_invoice = request.args.get("total_invoice")
    invoice = Invoice(invoice_id=invoice_id, customer_id=customer_id, employee_id=employee_id, date_of_invoice=date_of_invoice, total_invoice=total_invoice)
    db.session.add(invoice)
    db.session.commit()
    return render_template("insert_new_invoice_success.html")


#Thêm thông tin chi tiết hóa đơn
@app.route("/addNewInvoiceDetails")
def addNewInvoiceDetails():
    return render_template("insert_new_invoice_detail.html")


@app.route("/addNewInvoiceDetailsCommit")
def addNewInvoiceDetailsCommit():
    invoice_id = request.args.get("invoice_id")
    book_id = request.args.get("book_id")
    quantity = request.args.get("quantity")
    cost_book = request.args.get("cost_book")
    total = request.args.get("total")
    customer_id = request.args.get("customer_id")
    invoice_detail = Invoice_Details(invoice_id=invoice_id, book_id=book_id, quantity=quantity, cost_book=cost_book, total=total, customer_id=customer_id)
    db.session.add(invoice_detail)
    db.session.commit()
    return render_template("insert_new_invoice_details_success.html")


#Thêm thông tin vị trí làm việc
@app.route("/addNewWorkAt")
def addNewWorkAt():
    return render_template("insert_new_work_at.html")


@app.route("/addNewWorkAtCommit")
def addNewWorkAtCommit():
    employee_id = request.args.get("employee_id")
    number_book_shelf = request.args.get("number_book_shelf")
    work_ats = Work_at(employee_id=employee_id, number_book_shelf=number_book_shelf)
    db.session.add(work_ats)
    db.session.commit()
    return render_template("insert_new_work_at_success.html")


#Đọc thông tin khách hàng
@app.route("/show_All_Customer")
def showAllCustomer():
    customers = Customer.query.all()
    return render_template("show_all_customer.html", customers=customers)


#Đọc thông tin nhân viên
@app.route("/show_All_Employee")
def showAllEmployee():
    employees = Employee.query.all()
    return render_template("show_all_employee.html", employees=employees)


#Đọc thông tin kệ sách
@app.route("/show_All_BookShelf")
def showAllBookShelf():
    book_shelfs = Book_Shelf.query.all()
    return render_template("show_all_book_shelf.html", book_shelfs=book_shelfs)


#Đọc thông tin thể loại sách
@app.route("/show_All_Kind_of_book")
def show_All_Kind_of_book():
    kind_of_books = Kind_of_Book.query.all()
    return render_template("show_all_Kind_of_book.html", kind_of_books=kind_of_books)


#Đọc thông tin sách
@app.route("/show_All_Book")
def showAllBook():
    books = Book.query.all()
    return render_template("show_all_book.html", books=books)


#Đọc thông tin hóa đơn
@app.route("/show_All_Invoice")
def show_All_Invoice():
    invoices = Invoice.query.all()
    return render_template("show_all_invoice.html", invoices=invoices)


#Đọc thông tin chi tiết hóa đơn
@app.route("/show_All_Invoice_Details")
def Show_All_Invoice_Details():
    invoice_details = Invoice_Details.query.all()
    return render_template("show_all_invoice_details.html", invoice_details=invoice_details)


#Đọc thông tin chi tiết vị trí làm việc
@app.route("/show_All_Work_at")
def show_All_Work_at():
    work_ats = Work_at.query.all()
    return render_template("show_all_work_at.html", work_ats=work_ats)


#Tìm kiếm thông tin khách hàng
@app.route("/find_customer")
def find_customer():
    return render_template("find_customer.html")


@app.route("/find_customer_result") 
def find_customer_result():
    customer_id =request.args.get("customer_id")
    customer = Customer.query.get(customer_id)      
    return render_template("find_customer_result.html",customer=customer)


#Tìm kiếm thông tin nhân viên
@app.route("/find_employee")
def find_employee():
    return render_template("find_employee.html")


@app.route("/find_employee_result")
def find_employee_result():
    employee_id = int(request.args.get("employee_id"))
    employee = Employee.query.get(employee_id)      
    return render_template("find_employee_result.ht/ml",employee=employee)


#Tìm kiếm thông tin kệ sách
@app.route("/find_book_shelf")
def find_book_shelf():
    return render_template("find_book_shelf.html")


@app.route("/find_book_shelf_result")
def find_book_shelf_result():
    number = request.args.get("number")
    book_shelfs = Book_Shelf.query.get(number)      
    return render_template("find_book_shelf_result.html",book_shelfs=book_shelfs)


#Tìm kiếm thông tin thể loại sách
@app.route("/find_Kind_of_book")
def find_Kind_of_book():
    return render_template("find_Kind_of_book.html")


@app.route("/find_Kind_of_book_result")
def find_Kind_of_book_result():
    ID = request.args.get("id")
    kind_of_book = Kind_of_Book.query.get(ID)      
    return render_template("find_Kind_of_book_result.html",kind_of_book=kind_of_book)


#Tìm kiếm thông tin sách
@app.route("/find_book")
def find_book():
    return render_template("find_book.html")


@app.route("/find_book_result")
def find_book_result():
    book_id = request.args.get("book_id")
    book = Book.query.get(book_id)      
    return render_template("find_book_result.html",book=book)


#Tìm kiếm thông tin hóa đơn
@app.route("/find_invoice")
def find_invoice():
    return render_template("find_invoice.html")


@app.route("/find_invoice_result")
def find_invoice_result():
    invoice_id = request.args.get("invoice_id")
    invoice = Invoice.query.get(invoice_id)      
    return render_template("find_invoice_result.html",invoice=invoice)


#Tìm kiếm thông tin chi tiết hóa đơn
@app.route("/find_invoice_details")
def Find_invoice_details():
    return render_template("find_invoice_details.html")


@app.route("/find_invoice_details_result")
def Find_invoice_details_result():
    invoice_id = int(request.args.get("invoice_id"))
    invoice_details = Invoice_Details.query.filter_by(invoice_id=invoice_id).all()      
    return render_template("find_invoice_details_result.html",invoice_details=invoice_details)


#Tìm kiếm thông tin vị trí làm việc
@app.route("/find_work_at")
def find_work_at():
    return render_template("find_work_at.html")


@app.route("/find_work_at_result")
def find_work_at_result():
    employee_id = request.args.get("employee_id")
    work_at = Work_at.query.get(employee_id)      
    return render_template("find_work_at_result.html",work_at=work_at)


#Sửa thông tin khách hàng
@app.route("/infoCustomer")
def infoCustomer():
    customers = Customer.query.all()
    return render_template("update_customer.html", customers=customers)


@app.route("/update_customer_commit")
def update_customer_commit():
    customer_id = request.args.get("customer_id")
    customer = Customer.query.get(customer_id)
    customer.customer_name = request.args.get("customer_name")
    customer.address = request.args.get("address")
    customer.phone = request.args.get("phone")
    customer.email = request.args.get("email")
    db.session.commit()
    return render_template("update_customer_success.html")


#Sửa thông tin nhân viên
@app.route("/infoEmployee")
def infoEmployee():
    employees = Employee.query.all()
    return render_template("update_employee.html", employees=employees)


@app.route("/update_employee_commit")
def update_employee_commit():
    employee_id = request.args.get("employee_id")
    employee = Employee.query.get(employee_id)
    employee.employee_name = request.args.get("employee_name")
    employee.gender = request.args.get("gender")
    employee.birthday = request.args.get("birthday")
    employee.phone = request.args.get("phone")
    employee.email = request.args.get("email")
    employee.address = request.args.get("address")
    employee.position = request.args.get("position")
    employee.salary = request.args.get("salary")
    db.session.commit()
    return render_template("update_employee_success.html")


#Sửa thông tin kệ sách
@app.route("/infoBookShelf")
def infoBookShelf():
    book_shelfs = Book_Shelf.query.all()
    return render_template("update_bookshelf.html", book_shelfs=book_shelfs)


@app.route("/update_bookshelf_commit")
def update_bookshelf_commit():
    number = request.args.get("number")
    book_shelf = Book_Shelf.query.get(number)
    book_shelf.location = request.args.get("location")
    db.session.commit()
    return render_template("update_bookshelf_success.html")


#Sửa thông tin thể loại sách
@app.route("/info_Kind_of_book")
def info_Kind_of_book():
    kind_of_books = Kind_of_Book.query.all()
    return render_template("update_Kind_of_book.html", kind_of_books=kind_of_books)


@app.route("/update_Kind_of_book_commit")
def update_Kind_of_book_commit():
    ID = request.args.get("id")
    kind_of_book = Kind_of_Book.query.get(ID)
    kind_of_book.name = request.args.get("name")
    db.session.commit()
    return render_template("update_Kind_of_book_success.html")


#Sửa thông tin sách
@app.route("/infoBook")
def infoBook():
    books = Book.query.all()
    return render_template("update_book.html", books=books)


@app.route("/update_book_commit")
def update_book_commit():
    book_id = request.args.get("book_id")
    book = Book.query.get(book_id)
    book.name = request.args.get("book_name")
    book.authors = request.args.get("authors")
    book.publishing_year = request.args.get("publishing_year")
    book.kind_of_book = request.args.get("kind_of_book")
    book.cost = request.args.get("cost")
    book.quantity = request.args.get("quantity")
    db.session.commit()
    return render_template("update_book_success.html")


#Sửa thông tin hóa đơn
@app.route("/infoInvoice")
def infoInvoice():
    invoices = Invoice.query.all()
    return render_template("update_invoice.html", invoices=invoices)


@app.route("/update_invoice_commit")
def update_voice_commit():
    invoice_id = request.args.get("invoice_id")
    invoice = Invoice.query.get(invoice_id)
    invoice.customer_id = request.args.get("customer_id")
    invoice.employee_id = request.args.get("employee_id")
    invoice.date_of_invoice = request.args.get("date_of_invoice")
    invoice.total_invoice = request.args.get("total_invoice")
    db.session.commit()
    return render_template("update_invoice_success.html")


#Sửa thông tin chi tiết hóa đơn
@app.route("/infoInvoiceDetails")
def InfoInvoiceDetails():
    invoice_details = Invoice_Details.query.all()
    return render_template("update_invoice_details.html", invoice_details=invoice_details)


@app.route("/update_invoice_details_commit")
def Update_invoice_details_commit():
    invoice_id = request.args.get("invoice_id")
    book_id = request.args.get("book_id")
    new_book_id = request.args.get("new_book_id")  # thêm dòng này để lấy giá trị book_id mới
    invoice_detail = Invoice_Details.query.get((invoice_id, book_id)) 
    invoice_detail.book_id = new_book_id  # sử dụng book_id mới để cập nhật
    invoice_detail.quantity = request.args.get("quantity")
    invoice_detail.cost_book = request.args.get("cost_book")
    invoice_detail.customer_id = request.args.get("customer_id")
    db.session.commit()
    invoice_details = Invoice_Details.query.all()
    return render_template("update_invoice_details_success.html", invoice_details=invoice_details)


#Sửa thông tin vị trí làm việc
@app.route("/infoWor_kat")
def infoWork_at():
    work_ats = Work_at.query.all()
    return render_template("update_work_at.html", work_ats=work_ats)


@app.route("/update_work_at_commit")
def update_work_at_commit():
    employee_id = request.args.get("employee_id")
    work_at = Work_at.query.get(employee_id) 
    work_at.number_book_shelf = request.args.get("number_book_shelf")
    db.session.commit()
    return render_template("update_work_at_success.html")


#Xóa thông tin khách hàng
@app.route("/in_fo_Customer")
def in_fo_Customer():
    customers = Customer.query.all()
    return render_template("delete_customer.html",customers=customers)


@app.route("/delete_customer")
def delete_customer():
    customer_id = request.args.get("customer_id")
    customer = Customer.query.get(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return render_template("delete_customer_success.html")


#Xóa thông tin nhân viên
@app.route("/in_fo_Employee")
def in_fo_Employee():
    employees = Employee.query.all()
    return render_template("delete_employee.html",employees=employees)


@app.route("/delete_employee")
def delete_employee():
    employee_id = request.args.get("employee_id")
    employee = Employee.query.get(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return render_template("delete_employee_success.html")


#Xóa thông tin kệ sách
@app.route("/in_fo_BookShelf")
def in_fo_BookShelf():
    book_shelfs = Book_Shelf.query.all()
    return render_template("delete_bookshelf.html",book_shelfs=book_shelfs)


@app.route("/delete_bookshelf")
def delete_bookshelf():
    number = request.args.get("number")
    book_shelf = Book_Shelf.query.get(number)
    db.session.delete(book_shelf)
    db.session.commit()
    return render_template("delete_bookshelf_success.html")


#Xóa thông tin kệ sách
@app.route("/in_fo_Kind_of_book")
def in_fo_Kind_of_book():
    kind_of_books = Kind_of_Book.query.all()
    return render_template("delete_Kind_of_book.html",kind_of_books=kind_of_books)


@app.route("/delete_Kind_of_book")
def delete_Kind_of_book():
    ID = request.args.get("id")
    kind_of_book = Kind_of_Book.query.get(ID)
    db.session.delete(kind_of_book)
    db.session.commit()
    return render_template("delete_Kind_of_book_success.html")


#Xóa thông tin sách
@app.route("/in_fo_Book")
def in_fo_Book():
    books = Book.query.all()
    return render_template("delete_book.html",books=books)


@app.route("/delete_book")
def delete_book():
    book_id = request.args.get("book_id")
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return render_template("delete_book_success.html")


#Xóa thông tin hóa đơn
@app.route("/in_fo_Invoice")
def in_fo_Invoice():
    invoices = Invoice.query.all()
    return render_template("delete_invoice.html",invoices=invoices)


@app.route("/delete_invoice")
def delete_invoice():
    invoice_id = request.args.get("invoice_id")
    invoice = Invoice.query.get(invoice_id)
    db.session.delete(invoice)
    db.session.commit()
    return render_template("delete_invoice_success.html")


#Xóa thông tin chi tiết hóa đơn
@app.route("/in_fo_Invoice_Details")
def In_fo_Invoice_Details():
    invoice_details = Invoice_Details.query.all()
    return render_template("delete_invoice_details.html",invoice_details=invoice_details)


@app.route("/Delete_invoice_details")
def delete_invoice_details():
    invoice_id = request.args.get("invoice_id")
    book_id = request.args.get("book_id")
    invoice_detail = Invoice_Details.query.get((invoice_id, book_id)) 
    db.session.delete(invoice_detail)
    db.session.commit()
    return render_template("delete_invoice_details_success.html")


#Xóa thông tin vị trí làm việc
@app.route("/in_fo_Work_at")
def in_fo_Work_at():
    work_ats = Work_at.query.all()
    return render_template("delete_work_at.html",work_ats=work_ats)


@app.route("/delete_work_at")
def delete_work_at():
    employee_id = request.args.get("employee_id")
    work_at = Work_at.query.get(employee_id) 
    db.session.delete(work_at)
    db.session.commit()
    return render_template("delete_work_at_success.html")



if __name__== '__main__':
    app.run(debug=True)