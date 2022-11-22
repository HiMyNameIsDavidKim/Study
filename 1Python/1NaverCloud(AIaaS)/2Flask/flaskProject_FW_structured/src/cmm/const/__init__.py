import googlemaps
if __name__ == '__main__':
    gmaps = googlemaps.Client(key=".....")
    print(gmaps.geocode("대한민국 서울특별시 강남구 대치2동 514", language="ko"))