from api_response import ApiResponse

class NumberingApi:
    def request(self) -> ApiResponse:
        return ApiResponse()


if __name__ == '__main__':
    numbering_api = NumberingApi()
    api_response = numbering_api.request()
    print(api_response.next_id())