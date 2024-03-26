class ApiResponse:
    def __init__(self) -> None:
        self.id = 1

    def next_id(self):
        return str(self.id)
    

if __name__ == '__main__':
    api_response = ApiResponse()
    print(api_response.next_id())