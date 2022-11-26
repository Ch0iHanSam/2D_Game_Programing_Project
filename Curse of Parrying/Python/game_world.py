# layer 0 : Background Objects
# layer 1 : Foreground Objects
# layer 2 : Shields
# layer 3 : Attack Effects
# layer 4 : Button Objects
# layer 5 : UI Objects

objects = [ [], [], [], [], [], []]

def add_object(o, depth):  # 한 요소 해당 레이어(depth)에 추가
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol  # 여러 요소 해당 레이어에 추가 (리스트를 받아서 레이어 리스트에 요소들 추가시키기)

def remove_object(o):
    for layer in objects:
        try:  # 이 try except 말고 if o in layer를 사용해도 됨
            layer.remove(o)
            del o
            return
        except:
            pass  # except에서는 에러발생 시 pass를 진행한다는 뜻
    raise ValueError('Trying destroy non existing object')  # ValueError가 발생하면 멈추는게 아니라 '~' 출력하게끔 예외처리

def all_objects():
    for layer in objects:
        for o in layer:
            yield o  # return과 다르게 얘는 제너레이터를 반환함 (그게 뭐냐면)-> return은 결과를 다 모아서 메모리에 올려놓는데 yield는 하나 올리고 또 하나 올리고 한다는 차이.(리스트의 경우 결과를 나중에 한 번에 얻냐, 하나 하고 또 하나 하고냐 차이인데, 후자가 결과를 지속적으로 얻어서 체감상 더 빠르게 얻으니까 이게 더 좋은거임.)

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()