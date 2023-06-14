from bs4 import BeautifulSoup
import requests
import re
import csv


def table_scrape():
    url = 'https://e-ecolog.ru/buh/2020/2536133126'
    req = requests.get(url)

    soup = BeautifulSoup(req.content, "html.parser")
    table = soup.find("table", {"class": "bo mx-auto w-full"})

    table = table.findAll("tbody")[0]
    # Заголовок
    title_row = ['Year/Indicator(ths.rub.)', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013']

    # Основные средства - наименование
    fixed_assets_row = ['Fixed assets']

    # Итого по внеоборотным активам - наименование
    non_current_sum_row = ['Total for section I']

    # Запасы - наименование
    stocks_row = ["Stocks"]

    # НДС - наименование
    nds_row = ["VAT (value added tax)"]

    # Деб. задолженность - наименование
    dib_debt_row = ['Accounts receivable']

    # Финансовые вложения - наименование
    fin_attach_row = ["Financial investments"]

    # ДС и ДЭ - наименование
    cash_row = ["Cash and cash equivalents"]

    # Прочие оборотные активы - наименование
    other_current_assets_row = ["Other current assets"]

    # Итогу по оборотным активам - наименование
    current_sum_row = ["Total for section II"]

    # Общий баланс - наименование
    balance_row = ["BALANCE"]

    # Нераспределенная прибыль
    ret_earn_row = ["Retained earnings"]

    # Итого капитал и резервы - наименование
    sum_cap_row = ["Total for section III"]

    # Кредиторская задолженность - наименование
    acc_pay_row = ["Accounts payable"]

    for year in range(2020, 2012, -1):
        url_temp = f'https://e-ecolog.ru/buh/{year}/2536133126'
        req_temp = requests.get(url_temp)

        # Получаем значения для каждого показателя
        soup = BeautifulSoup(req_temp.content, "html.parser")
        table = soup.find("table", {"class": "bo mx-auto w-full"}).findAll("tbody")[0]

        # Значения каждого из показателей
        fixed_assets = re.sub('\s', '', table.find('td', string="Основные средства").findNext('td').findNext('td').text)
        non_current_sum = re.sub('\s', '',
                                 table.find('td', string="Итого по разделу I").findNext('td').findNext('td').text)
        stocks = re.sub('\s', '', table.find('td', string="Запасы").findNext('td').findNext('td').text)
        try:
            nds = re.sub('\s', '',
                         table.find('td', string="Налог на добавленную стоимость по приобретенным ценностям").findNext(
                             'td').findNext('td').text)
        except AttributeError:
            nds = '0'
        dib_debt = re.sub('\s', '',
                          table.find('td', string="Дебиторская задолженность").findNext('td').findNext('td').text)
        try:
            fin_attach = re.sub('\s', '', table.find('td',
                                                     string="Финансовые вложения (за исключением денежных эквивалентов)").findNext(
                'td').findNext('td').text)
        except AttributeError:
            fin_attach = '0'
        cash = re.sub('\s', '',
                      table.find('td', string="Денежные средства и денежные эквиваленты").findNext('td').findNext(
                          'td').text)
        other_current_assets = re.sub('\s', '',
                                      table.find('td', string="Прочие оборотные активы").findNext('td').findNext(
                                          'td').text)
        current_sum = re.sub('\s', '',
                             table.find('td', string="Итого по разделу II").findNext('td').findNext('td').text)
        balance = re.sub('\s', '', table.find('td', string="БАЛАНС").findNext('td').findNext('td').text)
        ret_earn = re.sub('\s', '', table.find('td', string="Нераспределенная прибыль (непокрытый убыток)").findNext(
            'td').findNext('td').text)
        sum_cap = re.sub('\s', '', table.find('td', string="Итого по разделу III").findNext('td').findNext('td').text)
        acc_pay = re.sub('\s', '',
                         table.find('td', string="Кредиторская задолженность").findNext('td').findNext('td').text)

        fixed_assets_row.append(fixed_assets)
        non_current_sum_row.append(non_current_sum)
        stocks_row.append(stocks)
        nds_row.append(nds)
        dib_debt_row.append(dib_debt)
        fin_attach_row.append(fin_attach)
        cash_row.append(cash)
        other_current_assets_row.append(other_current_assets)
        current_sum_row.append(current_sum)
        balance_row.append(balance)
        ret_earn_row.append(ret_earn)
        sum_cap_row.append(sum_cap)
        acc_pay_row.append(acc_pay)

    raw_data = [title_row, fixed_assets_row, non_current_sum_row, stocks_row, nds_row, dib_debt_row, fin_attach_row,
                cash_row, other_current_assets_row, current_sum_row, balance_row, ret_earn_row, sum_cap_row,
                acc_pay_row]

    with open("output_data.csv", "w+") as f:
        writer = csv.writer(f)
        writer.writerows(raw_data)


'''
print(df)
print(df.loc[4, :].tolist()[0:])
print(df.columns.tolist()[:])
'''
