module.exports = function getZerosCount(number, base) {
  // your implementation
  //if (1 <= number <= 10^7 && 2 <= base <= 256) {
    let i = 2;
    let b = base;
    let dividers = [];
    let degrees = [];
    let ps_i = 0;
    let step = 0;

    while (i <= base) {
      if (b % i == 0) {
        if (i > ps_i) {
          degrees.push(step)
          dividers.push(i)
          ps_i = i
          step = 0
        }
        // console.log('b =', b, 'i = ', i);
        b /= i
        step += 1                
      }
      else {
        i +=1  
      }
    }   
    degrees.push(step)
    degrees.shift()
    // console.log(dividers,degrees);
    
    function countdel(delit, stepen) {
      let temp = number;
      let count = 0;
      let i = delit;

      while (parseFloat(temp / i) > 1) {
        count += parseInt(temp  / i);
        // console.log('c',count,'i = ', i);
        // console.log('delit',delit);
        i *= delit;
      }
      count = Math.round(parseFloat(count / stepen));
      return count;
    }

    variants = []
    for (let i = 0; i < dividers.length; i++) {
      variants.push(countdel(dividers[i],degrees[i]))
    }
    // console.log(variants);

    return Math.min.apply(null, variants);
  //}
}