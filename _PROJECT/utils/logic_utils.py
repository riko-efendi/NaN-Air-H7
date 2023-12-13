from datetime import datetime, timedelta

DATE_FORMAT ="%Y-%m-%d"

class LogicUtils:
    def generate_date_range(self, start_date_str, end_date_str):
        start_date = datetime.strptime(start_date_str, DATE_FORMAT)
        end_date = datetime.strptime(end_date_str, DATE_FORMAT)

        date_list = []
        current_date = start_date

        while current_date <= end_date:
            date_list.append(current_date.strftime(DATE_FORMAT))
            current_date += timedelta(days=1)

        return date_list

