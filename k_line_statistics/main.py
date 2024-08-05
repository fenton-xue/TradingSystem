from datetime import datetime

from data_provider.data_provider import DataProvider
from utils.make_excel import MakeExcel


def main():
    # 用户定义币种
    trading_target = input("请输入交易币种（例如BTC）: ")
    trading_target_usdt = trading_target + "/USDT"
    data_provider = DataProvider(symbol=trading_target_usdt)  # 创建数据提供类实例

    # 用户选择统计的K线类型
    pinbar_or_doji_select_number = input("请输入你想统计的K线类型（Pinbar：1 | Doji：2）:")
    if pinbar_or_doji_select_number == "1":
        make_excel = MakeExcel("Pinbar")
    elif pinbar_or_doji_select_number == "2":
        make_excel = MakeExcel("Doji")
    else:
        print("输入有误，程序结束！")
        return

    # 用户选择小数点位数
    point_number = input("请输入小数点位数（例如2）: ")

    while True:
        user_input = input("请输入时间 (格式为:2024-08-04T10:00:00Z), 输入0删除最后一行数据, 输入-1退出: ")
        if user_input == "-1":
            break
        elif user_input == "0":
            make_excel.delete_last_row()
        else:
            try:
                data = data_provider.fetch_single_data(user_input, point_number)  # 获取数据
                if data not in [None, []]:
                    make_excel.write_dict_to_existing_excel(data)
                    print("数据已写入Excel文件")
                else:
                    print("未能获取到K线数据")
            except ValueError:
                print("输入有误，请重新输入！")


if __name__ == "__main__":
    main()

