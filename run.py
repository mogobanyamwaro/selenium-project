from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        print('exiting..')
        bot.select_place_to_go('New York')
        bot.select_dates('2021-11-06', '2021-11-12')
        bot.select_adults(10)
        bot.click_search()
        bot.apply_filtrations()
except Exception as e:
    print("Problem found")
