var mergeAlternately = function(word1, word2) {
    let i = 0;
    let j = 0;
    let res = '';
    while (i < word1.length && j < word2.length) {
    res += word1[i];
    res += word2[j];
    i++;
    j++;
    }
    res += word1.slice(i);
    res+ word2.slice(j);

    return res
    
    
};

console.log(mergeAlternately('abc', 'phr'))