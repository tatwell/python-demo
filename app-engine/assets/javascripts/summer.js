
$(document).ready(function() {
  var randInt = function(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  };

  var randomNumberSet = function(setSize, min, max) {
    var numberSet = [];

    for (var n=0; n<setSize; n++) {
      numberSet.push(randInt(min, max));
    }

    console.debug('Generate random number set of', numberSet.length, 'integers');
    return numberSet;
  };

  var randomTarget = function(numberSet) {
    var sampleSize = randInt(1, numberSet.length);
    var targetSet = [];

    while ( sampleSize > 0 ) {
      var i = randInt(0, numberSet.length-1);
      var number = numberSet[i];
      targetSet.push(number);
      sampleSize--;
    }

    var targetSum = targetSet.reduce(function(pv, cv) { return pv + cv; }, 0);
    console.debug('Generated sum', targetSum, 'from subset of', targetSet.length, 'numbers.');
    return targetSum
  };

  $('button#test').on('click', function() {
    var setSize = randInt(20, 100);
    var numberSet = randomNumberSet(setSize, 1, 1000);
    var target = randomTarget(numberSet);

    $('textarea#numbers').val(numberSet.join(' '));
    $('input#target').val(target);
  });
});
