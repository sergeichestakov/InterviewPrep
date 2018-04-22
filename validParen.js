/**
 * @param {string} s
 * @return {boolean}
 */
const map = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
}

const isValid = s => {
    //odd cannot be valid
    if(s.length % 2){return false}

    let stack = []

    for(character of s){
        if(character in map){
            stack.push(character)
        } else {
            let opposing = stack.pop();
            if(map[opposing] != character){
                return false;
            }
        }
    }

    return !stack.length;
};
