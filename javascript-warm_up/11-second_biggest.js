#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const nums = args.map(Number);
  // use sort() method to sort nums in ascending order
  nums.sort((a, b) => b - a);
  // nums[1] = second num
  console.log(nums[1]);
}
