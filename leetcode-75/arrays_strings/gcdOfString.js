/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    let str1_len = str1.length;
    let str2_len = str2.length;
    // console.log(st)
    if (str1_len > str2_len) {
        gcdOfStrings(str2, str1);
    }
    for (let i = Math.min(str1_len, str2_len); i > 0; i --) {
        let sub_str = str1.slice(i);
        sub_str_len = sub_str.length;
        if (str1_len % sub_str_len == 0 || str2_len % sub_str_len == 0){
            let div1 = str1_len / sub_str_len;
            let div2 = str2_len / sub_str_len;
            
            // console.log("I m herer",sub_str.repeat(div1),sub_str.repeat(div2))
            if ( sub_str.repeat(div1) == str1 && sub_str.repeat(div2) == str2) {
                return sub_str
            }
        }
        else {

        }
    }
    return ""
}
console.log(gcdOfStrings(
     'CTCXKCTCXKCTCXKCTCXKCTCXKCTCXKCTCXKCTCXKCTCXKCTCXKCTCXK',
    'CTCXKCTCXKCTCXKCTCXKCTCXKCTCXKCTCXKCTCXKCTCXK',
    ))

console.log(gcdOfStrings(
    'ABABABAB',
    'ABAB'
))