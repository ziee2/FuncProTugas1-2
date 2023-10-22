// kode 1
var sequenceGenerator = (int start, int stop) =>  List<int>.generate((stop - start) + 1, (index) => start+index);

// kode 2
var fizzBuzz = (int a, int b) =>  List.generate((b - a) + 1, (index) => a + index).map((num) => num % 3 == 0 && num % 5 == 0 ? 'FizzBuzz' : num % 3 == 0 ? 'Fizz' : num % 5 == 0 ? 'Buzz' : num).toList();

// kode 3
var twoNumber = (List<int> l) => l.map((i) => l.indexOf(i) == l.length - 1 ? null : i + l[l.indexOf(i) + 1]).toList().where((element) => element != null).toList(); 


void main(){
  print(sequenceGenerator(1, 10));
  print(fizzBuzz(1, 10));
  print(twoNumber([2, 4, 0, 7]));
}