function convertToRoman(num) {
  let lookupTable1 = {
    "0": "",
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
  }
  let lookupTable2 = {
    "0": "",
    "10": "X",
    "20": "XX",
    "30": "XXX",
    "40": "XL",
    "50": "L",
    "60": "LX",
    "70": "LXX",
    "80": "LXXX",
    "90": "XC",
    "100": "C",
    "200": "CC",
    "300": "CCC",
    "400": "CD",
    "500": "D",
    "600": "DC",
    "700": "DCC",
    "800": "DCCC",
    "900": "CM",
    "1000": "M",
    "2000": "MM",
    "3000": "MMM",
    "4000": "MMMM",
    "5000": "MMMMM",
    "6000": "MMMMMM",
    "7000": "MMMMMMM",
    "8000": "MMMMMMMM",
    "9000": "MMMMMMMMM",
  }
 // code for single digit numbers
if (num.toString().length == 1) {
  return lookupTable1[num.toString()];
  // code for double digit numbers 
} else if (num.toString().length === 2) {
  let roman_num = []
  let first_num = num.toString()[0] + "0";
  let first_num_roman = lookupTable2[first_num]
  roman_num.push(first_num_roman)
  let second_num = num.toString()[1]
  let second_num_roman = lookupTable1[second_num]
  roman_num.push(second_num_roman)
  let newv = roman_num.join("")
  console.log(newv)
  return newv
  // code for triple digit numbers
} else if (num.toString().length === 3) {
  let roman_num = []
  let first_num = num.toString()[0] + "00"
  let first_num_roman = lookupTable2[first_num]
  roman_num.push(first_num_roman)
  let second_num = num.toString()[1] + "0"
  let second_num_roman = lookupTable2[second_num]
  roman_num.push(second_num_roman);
  let third_num = num.toString()[2] 
  let third_num_roman = lookupTable1[third_num]
  roman_num.push(third_num_roman)
  let newv = roman_num.join("")
  console.log(newv)
  return newv
  // code for 4 digit numbers
  } else if (num.toString().length === 4) {
    let roman_num = []
    let first_num = num.toString()[0] + "000"
    let first_num_roman = lookupTable2[first_num]
    roman_num.push(first_num_roman)
    let second_num = num.toString()[1] + "00"
    let second_num_roman = lookupTable2[second_num]
    roman_num.push(second_num_roman);
    let third_num = num.toString()[2] + "0"
    let third_num_roman = lookupTable2[third_num]
    roman_num.push(third_num_roman)
    let fourth_num = num.toString()[3]
    let fourth_num_roman = lookupTable1[fourth_num]
    roman_num.push(fourth_num_roman)
    let newv = roman_num.join("")
    console.log(newv)
    return newv
    

  }
}
