def sqrt_n_times(x, n): 
    #คนืค่าทเี่สมอืนการนาค่าในxมากดป่มุ เป็นจานวนnครงั้
    for i in range(n):
        x = x**.5
    return x

def cube_root(y):
    #คนื ค่าประมาณของรากทสี่ ามของyโดยใชว้ธิ ที เ่ีสมอื นการกดป่มุ ดว้ยสูตร # y(1/22)(1+1/22)(1+1/24)(1+1/28)(1+1/216)(1+1/232)
    # ขอ้ แนะนา: เรียกใชฟ้ ังกช์ ัน sqrt_n_times
    a = sqrt_n_times(y, 2)
    for i in range(5):
        a = a * sqrt_n_times(a,2**(i+1))
    return a


def main():
    q = float(input()) 
    print(cube_root(q))

exec(input()) # DON'T remove this line