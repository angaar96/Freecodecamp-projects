function rot13(str) {

  let conversionTable = {
    "A": "N",
    "B": "O",
    "C": "P",
    "D": "Q",
    "E": "R",
    "F": "S",
    "G": "T",
    "H": "U",
    "I": "V",
    "J": "W",
    "K": "X",
    "L": "Y",
    "M": "Z", 
    "N": "A", 
    "O": "B", 
    "P": "C",
    "Q": "D", 
    "R": "E",
    "S": "F",
    "T": "G",
    "U": "H",
    "V": "I",
    "W": "J",
    "X": "K",
    "Y": "L",
    "Z": "M",
  }
  
  let converted = ""
  let regex = /[\W]/g
  for (let i=0; i<str.length; i++) {
    if (regex.test(str[i]) === true) {
      converted += str[i]
    } else {
      converted += conversionTable[str[i]]
      }
  }
  console.log(converted); 
  return converted
