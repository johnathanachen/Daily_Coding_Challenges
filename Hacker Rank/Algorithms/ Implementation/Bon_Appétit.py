def bonAppetit(n, k, b, ar):
    item_to_remove = ar[k]
    ar.pop(k)
    sum_of_bill = sum(ar)
    each_person = int(sum_of_bill/2)
    if each_person == b:
         return "Bon Appetit"
    else:
        refund_amount = b - each_person
        return refund_amount

def main():
    n,k =[4,1]
    ar = [3,10,2,9]
    b = 12
    result = bonAppetit(n, k, b, ar)
    print(result)

main()
