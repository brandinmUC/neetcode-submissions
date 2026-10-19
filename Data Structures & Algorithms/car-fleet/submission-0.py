class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        cars = [[0]] * len(position)
        
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars[i] = [position[i], time]
        cars.sort(key=lambda x: x[0])
       
        localmax = 0
        while cars:
            car = cars.pop()
            car_speed = car[1]
            if car_speed > localmax:
                localmax = car_speed
                res += 1
        return res
