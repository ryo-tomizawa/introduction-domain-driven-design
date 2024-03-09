class ModelNumber:
    def __init__(self, product_code: str, branch: str, lot: str) -> None: 
        if product_code is None: raise ValueError(f'error valueof product_code: {product_code}')
        if branch is None: raise ValueError(f'error valueof product_code: {branch}')
        if lot is None: raise ValueError(f'error valueof product_code: {lot}')

        self.product_code = product_code
        self.branch = branch
        self.lot = lot

    def __str__(self) -> str:
        return self.product_code + '-' + self.branch + '-' + self.lot
    

if __name__ == '__main__':
    model_number = ModelNumber('aaa', 'bbb', 'ccc')
    print(model_number)