'''Write two functions that convert a roman numeral to and from an integer value. 
Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately 
starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four

EXAMPLES
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1
'''
class RomanNumerals:
    
    @staticmethod
    def to_roman(val: int) -> str:
        VAL_DICT = {
            1000 : 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5 : 'V',
            4 : 'IV',
            1 : 'I'
        }
        result = ''
        for num, roman in VAL_DICT.items():
            while val >= num:
                result += roman
                val -= num
        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        ROMAN = {
            'M' : 1000, 
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
        }
        vals = list(map(lambda x: ROMAN[x], roman_num))
        val = 0
        for i,v in enumerate (vals):
            n = vals[i+1] if i < (len(vals)-1) else 0
            val = val-v if v < n else val+v
        return val
    
r_to_n = 'MCMXLIV'
print (RomanNumerals.from_roman(r_to_n))
n_to_r = 2945

print (RomanNumerals.to_roman(n_to_r))