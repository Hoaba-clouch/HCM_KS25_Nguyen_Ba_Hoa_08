vehicles = [
    {
        "vehicle_id": "XE001",
        "license_plate": "29C-12345",
        "driver_name": "Tài A",
        "fuel_standard": 12,
        "total_km": 500,
        "actual_fuel": 65,
        "deviation": 5.0,
        "status": "Tiêu hao cao"
    }
]

def calculate_deviation(fuel_standard, total_km, actual_fuel):
    theoretical_fuel = (total_km * fuel_standard) / 100
    return actual_fuel - theoretical_fuel


def classify_performance(deviation):
    if deviation < 0:
        return "Tiết kiệm"
    elif deviation < 2:
        return "Tiêu chuẩn"
    elif deviation < 8:
        return "Tiêu hao cao"
    else:
        return "Quá tải / Thất thoát"

def find_vehicle_by_id(vehicle_id):
    for vehicle in vehicles:
        if vehicle["vehicle_id"].lower() == vehicle_id.lower():
            return vehicle
    return None


def input_non_empty_string(message):
    while True:
        value = input(message).strip()
        if value != "":
            return value
        print("Dữ liệu không được để trống!")


def input_number(message, min_value=0, allow_zero=True):
    while True:
        try:
            value = float(input(message))
            if allow_zero and value >= min_value:
                return value
            if not allow_zero and value > min_value:
                return value
            print("Giá trị nhập không hợp lệ!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")


def display_vehicle(vehicle):
    print(
        f"{vehicle['vehicle_id']:<10}"
        f"{vehicle['license_plate']:<15}"
        f"{vehicle['driver_name']:<15}"
        f"{vehicle['fuel_standard']:<12}"
        f"{vehicle['total_km']:<12}"
        f"{vehicle['actual_fuel']:<15}"
        f"{vehicle['deviation']:<15.2f}"
        f"{vehicle['status']:<25}"
    )


def display_vehicle_list():
    print("\nDANH SÁCH ĐỘI XE")

    if len(vehicles) == 0:
        print("Danh sách đội xe đang trống!")
        return

    print("-" * 119)
    print(
        f"{'Mã xe':<10}"
        f"{'Biển số':<15}"
        f"{'Tài xế':<15}"
        f"{'Định mức':<12}"
        f"{'Tổng KM':<12}"
        f"{'Nhiên liệu':<15}"
        f"{'Chênh lệch':<15}"
        f"{'Trạng thái':<25}"
    )
    print("-" * 119)
    for vehicle in vehicles:
        display_vehicle(vehicle)

    print("-" * 119)

def add_vehicle():
    print("\nTHÊM XE MỚI")
    while True:
        vehicle_id = input_non_empty_string("Nhập mã xe: ")
        if find_vehicle_by_id(vehicle_id) is None:
            break
        print("Mã xe đã tồn tại, vui lòng nhập mã khác!")
    license_plate = input_non_empty_string("Nhập biển số xe: ")
    driver_name = input_non_empty_string("Nhập tên tài xế: ")

    fuel_standard = input_number("Nhập định mức lý thuyết (lít/100km): ", 0, False)
    total_km = input_number("Nhập tổng số km đã di chuyển: ", 0, True)
    actual_fuel = input_number("Nhập tổng nhiên liệu tiêu thụ thực tế: ", 0, True)

    deviation = calculate_deviation(fuel_standard, total_km, actual_fuel)
    status = classify_performance(deviation)

    new_vehicle = {
        "vehicle_id": vehicle_id,
        "license_plate": license_plate,
        "driver_name": driver_name,
        "fuel_standard": fuel_standard,
        "total_km": total_km,
        "actual_fuel": actual_fuel,
        "deviation": deviation,
        "status": status
    }

    vehicles.append(new_vehicle)
    print("Thêm xe mới thành công!")

def update_vehicle():
    print("\nCẬP NHẬT NHẬT KÝ HÀNH TRÌNH")
    vehicle_id = input_non_empty_string("Nhập mã xe cần cập nhật: ")
    vehicle = find_vehicle_by_id(vehicle_id)

    if vehicle is None:
        print("Không tìm thấy mã phương tiện!")
        return

    print("Thông tin xe hiện tại:")
    print("-" * 119)
    print(
        f"{'Mã xe':<10}"
        f"{'Biển số':<15}"
        f"{'Tài xế':<15}"
        f"{'Định mức':<12}"
        f"{'Tổng KM':<12}"
        f"{'Nhiên liệu':<15}"
        f"{'Chênh lệch':<15}"
        f"{'Trạng thái':<25}"
    )
    print("-" * 119)
    display_vehicle(vehicle)
    print("-" * 119)

    vehicle["fuel_standard"] = input_number("Nhập định mức lý thuyết mới: ", 0, False)
    vehicle["total_km"] = input_number("Nhập tổng số km mới: ", 0, True)
    vehicle["actual_fuel"] = input_number("Nhập tổng nhiên liệu tiêu thụ mới: ", 0, True)

    vehicle["deviation"] = calculate_deviation(
        vehicle["fuel_standard"],
        vehicle["total_km"],
        vehicle["actual_fuel"]
    )
    vehicle["status"] = classify_performance(vehicle["deviation"])
    print("Cập nhật nhật ký hành trình thành công!")

def delete_vehicle():
    print("\nXÓA XE KHỎI ĐỘI QUẢN LÝ")

    vehicle_id = input_non_empty_string("Nhập mã xe cần xóa: ")
    vehicle = find_vehicle_by_id(vehicle_id)

    if vehicle is None:
        print("Không tìm thấy mã xe!")
        return
    confirm = input("Bạn có chắc muốn xóa phương tiện này khỏi đội xe không? (Y/N): ").strip().lower()
    if confirm == "y":
        vehicles.remove(vehicle)
        print("Xóa xe thành công!")
    else:
        print("Đã hủy thao tác xóa!")

def search_vehicle():
    print("\nTÌM KIẾM PHƯƠNG TIỆN")
    keyword = input_non_empty_string("Nhập mã xe, biển số hoặc tên tài xế cần tìm: ")
    results = []
    exact_vehicle = find_vehicle_by_id(keyword)
    if exact_vehicle is not None:
        results.append(exact_vehicle)
    else:
        for vehicle in vehicles:
            if (
                keyword.lower() in vehicle["license_plate"].lower()
                or keyword.lower() in vehicle["driver_name"].lower()
            ):
                results.append(vehicle)

    if len(results) == 0:
        print("Không tìm thấy phương tiện phù hợp!")
        return

    print("\nKẾT QUẢ TÌM KIẾM")
    print("-" * 119)
    print(
        f"{'Mã xe':<10}"
        f"{'Biển số':<15}"
        f"{'Tài xế':<15}"
        f"{'Định mức':<12}"
        f"{'Tổng KM':<12}"
        f"{'Nhiên liệu':<15}"
        f"{'Chênh lệch':<15}"
        f"{'Trạng thái':<25}"
    )
    print("-" * 119)
    
    for vehicle in results:
        display_vehicle(vehicle)

    print("-" * 119)

def fleet_statistics():
    saving = 0
    standard = 0
    high = 0
    overload = 0

    for vehicle in vehicles:
        if vehicle["status"] == "Tiết kiệm":
            saving += 1
        elif vehicle["status"] == "Tiêu chuẩn":
            standard += 1
        elif vehicle["status"] == "Tiêu hao cao":
            high += 1
        else:
            overload += 1

    print(f"Tiết kiệm: {saving}")
    print(f"Tiêu chuẩn: {standard}")
    print(f"Tiêu hao cao: {high}")
    print(f"Quá tải / Thất thoát: {overload}")
    
while True:
    header = "HỆ THỐNG QUẢN LÝ ĐỘI XE LOGISTICS".center(50, "=")
    menu = '''
1. Hiển thị danh sách đội xe
2. Bổ sung xe mới vào đội
3. Cập nhật nhật ký hành trình
4. Xóa xe khỏi đội quản lý
5. Tìm kiếm phương tiện
6. Thống kê hiệu suất hạm đội
7. Phân loại hiệu suất tự động
8. Thoát chương trình
'''
    menu_footer = "=" * len(header)
    print(f"{header}{menu}{menu_footer}")
    choice = input("Mời bạn chọn chức năng (1-8): ").strip()

    match choice:
        case "1":
            display_vehicle_list()

        case "2":
            add_vehicle()

        case "3":
            update_vehicle()

        case "4":
            delete_vehicle()

        case "5":
            search_vehicle()

        case "6":
            fleet_statistics()

        case "7":
            print("Hệ thống đã tự động phân loại hiệu suất khi thêm hoặc cập nhật dữ liệu.")

        case "8":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")