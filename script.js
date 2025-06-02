function floatToBinary(f) {
  const integerPart = Math.floor(f);
  let binaryIntegerPart = integerPart.toString(2);

  let fractionalPart = f - integerPart;
  let binaryFractionalPart = "";

  let count = 0;
  while (fractionalPart !== 0 && count < 52) {
    fractionalPart *= 2;
    binaryFractionalPart += Math.floor(fractionalPart).toString();
    fractionalPart -= Math.floor(fractionalPart);
    count++;
  }

  return binaryIntegerPart + "." + binaryFractionalPart;
}

function padZeros(str, length) {
  return str + "0".repeat(length - str.length);
}

function convert() {
  const input = document.getElementById("input-number").value.trim();
  const outputElem = document.getElementById("output");
  const binaryElem = document.getElementById("binary-output");

  if (input === "") {
    outputElem.innerText = "No input given.";
    return;
  }

  let n = parseFloat(input);
  let s = n < 0 ? 1 : 0;
  if (n < 0) n = -n;

  let a = floatToBinary(n);
  binaryElem.innerText = a;

  let result = "";

  if (n > 0 && n < 1) {
    let ind = a.indexOf("1");
    let aScaled = parseFloat(a.replace(".", "")) * 10 ** (ind - 1);
    let aStr = aScaled.toString();
    let z = aStr.replace(".", "");

    let man = z.substring(1, 24);
    man = padZeros(man, 23);
    let e1 = (127 - (ind - 1)).toString(2).padStart(8, "0");

    result += `32-bit Single Precision\n`;
    result += `S E        M\n`;
    result += `${s} ${e1} ${man}\n\n`;

    man = z.substring(1, 53);
    man = padZeros(man, 52);
    e1 = (1023 - (ind - 1)).toString(2).padStart(11, "0");

    result += `64-bit Double Precision\n`;
    result += `S E           M\n`;
    result += `${s} ${e1} ${man}`;
  } else if (n >= 1) {
    let ind = a.indexOf(".");
    let z = a.replace(".", "");
    let man = z.substring(1, 24);
    man = padZeros(man, 23);
    let e1 = (127 + (ind - 1)).toString(2).padStart(8, "0");

    result += `32-bit Single Precision\n`;
    result += `S E        M\n`;
    result += `${s} ${e1} ${man}\n\n`;

    man = z.substring(1, 53);
    man = padZeros(man, 52);
    e1 = (1023 + (ind - 1)).toString(2).padStart(11, "0");

    result += `64-bit Double Precision\n`;
    result += `S E           M\n`;
    result += `${s} ${e1} ${man}`;
  }

  outputElem.innerText = result;
}
