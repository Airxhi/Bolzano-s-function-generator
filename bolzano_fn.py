import matplotlib.pyplot as plt
import sys

def calculate_interval_points(k, a, b, A, B):
    if k == 0:
        return [(a,A),(b,B)]
    if k > 1:
        q1 = calculate_interval_points(k-1, a, a + 3.0/8.0 * (b - a), A, A + 5.0/8.0*(B-A)) 
        q2 = calculate_interval_points(k-1, a + 3.0/8.0 * (b - a), (a+b)/2.0, A + 5.0/8.0*(B-A), (A+B)/2.0)
        q3 = calculate_interval_points(k-1, (a+b)/2.0, a+7.0/8.0*(b-a), (A+B)/2.0, B + 1.0/8.0*(B-A))
        q4 = calculate_interval_points(k-1, a+7.0/8.0*(b-a), b, B + 1.0/8.0*(B-A), B)

        return q1+q2+q3+q4

    return [(a,A), (a + 3.0/8.0 * (b - a),A+5.0/8.0*(B-A)), ((a+b)/2.0, A + (B-A)/2.0), (a + 7.0/8.0 * (b - a), B + 1/8*(B-A)), (b,B)]

def main():
    if len(sys.argv) < 6:
        print("format: python3 " + sys.argv[0] + " k a b A B [show_k1]")
        exit()

    k = int(sys.argv[1])
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    A = int(sys.argv[4])
    B = int(sys.argv[5])

    show_k1 =  False

    if (len(sys.argv) == 7):
        show_k1 = bool(sys.argv[6])

    k-=1

    if k < 0:
        print (">:(")
        exit()

    x_vals = []
    y_vals = []

    x2_vals = []
    y2_vals = []

    points = calculate_interval_points(k, a, b, A, B)
    points2 = calculate_interval_points(1, a, b, A, B)

    for point in points2:
        x2_vals.append(point[0])
        y2_vals.append(point[1])

    for point in points:
        x_vals.append(point[0])
        y_vals.append(point[1])

    plt.plot(x_vals, y_vals)
    if show_k1:
        plt.plot(x2_vals, y2_vals, linestyle='dashed')
    plt.plot([a,b],[A,B], linestyle='dashed')
    plt.title("Bolzano's function for k=" + str(k+1))
    plt.xlabel('x')
    plt.ylabel('Bk(x)')
    plt.savefig('out.png', figsize='(1920,1080)')
    plt.show()  

main()
    


