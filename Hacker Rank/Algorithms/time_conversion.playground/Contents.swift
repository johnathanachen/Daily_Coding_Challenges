//: Playground - noun: a place where people can play

import UIKit



func timeConversion() {
    let s = "07:05:45PM"
    var arr_str = Array(s)
    print(arr_str)
    if arr_str.contains("P") {
        var time_value = arr_str[1]
        print(time_value + 12)
    }
    
}

timeConversion()
