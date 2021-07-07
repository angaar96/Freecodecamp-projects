function palindrome(str) {
  const anumeric = str.toLowerCase().match(/[a-z0-9]/g);
  let clone_anumeric = [...anumeric]
  let clone_reversed = clone_anumeric.reverse()
  return clone_reversed.join("") === anumeric.join("")
