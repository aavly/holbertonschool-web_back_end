export default function returnHowManyArguments(...argsss) {
  let total = 0;
  for (const arg of argsss) {
    total += 1;
  }
  return total;
}
