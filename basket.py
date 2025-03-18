class Basket:
    def __init__(self,name:str):
        self.name = name
        self.arr = []
        self.add_check = 0

    def add_item(self,value:str):
        self.arr.append(value)


    def __len__(self):
        return len(self.arr)


    def __getitem__(self,key):
        return self.arr[key]   


    def __setitem__(self,key,value):
        self.arr[key] = value


    def __iter__(self):
        return iter(self.arr)


    def __add__(self,other):
        add_name = f"{self.name}과 {other.name}"
        new_basket = Basket(add_name)
        new_basket.arr = self.arr+other.arr
        new_basket.add_check = 1
        return new_basket
    
    def __eq__(self,other):
        if self.arr == other.arr:
            return True
        else:
            return False
        
    def __enter__(self):
        return self
    

    def __exit__(self,exc_type,exc_value,traceback):
        print("장바구니 사용 종료!")
        return self       
        
    
    
    

    def __str__(self):
        if self.add_check == 0:
            return str(f"{self.name}의 장바구니: {self.arr}")    
        else:
            return str(f"{self.name}의 합친 장바구니: {self.arr}")


basket1 = Basket("홍길동")
basket1.add_item("사과")
basket1.add_item("바나")
print(basket1) 
print(len(basket1))
print(basket1[0])
basket1[1] = "딸기"
print(basket1)

for item in basket1:
    print(item)

basket2 = Basket("김철수")
basket2.add_item("딸기")

basket3 = basket1 + basket2
print(basket3)

print(basket1 == basket2)

with basket1:
    print("장바구니 사용중")