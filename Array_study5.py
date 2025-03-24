class Basket:
    def __init__(self, name: str):
        self.name = [name]
        self.arr = []

    def add_item(self, value: str):
        self.arr.append(value)

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, key):
        return self.arr[key]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __iter__(self):
        return iter(self.arr)

    def __add__(self, other):
        new_basket = Basket(self.name[0])
        new_basket.name.extend(name for name in other.name)
        new_basket.arr = self.arr + other.arr
        return new_basket
    
    def __sub__(self, other):
        new_basket = Basket(f"{self.name[0]}에서 {other.name[0]} 뺀")
        new_basket.arr = [item for item in self.arr if item not in other.arr]
        return new_basket

    def __eq__(self, other):
        return self.arr == other.arr

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("장바구니 사용 종료!")
        return self

    def __str__(self):
        length = len(self.name)
        if length == 1:
            return f"{self.name[0]}의 장바구니: {self.arr}"
        elif length == 2:
            return f"{self.name[0]}과 {self.name[1]}의 합친 장바구니: {self.arr}"
        else:
            return f"{self.name[0]} 외 {length - 1}명의 합친 장바구니: {self.arr}"



basket1 = Basket("홍길동")
basket1.add_item("사과")
basket1.add_item("바나나")

print(basket1)

basket2 = Basket("김철수")
basket2.add_item("딸기")

print(basket2)

basket3 = basket1 - basket2

print(basket3)
basket4 = Basket("임건우")
basket4.add_item("복숭아")

print(basket4)
