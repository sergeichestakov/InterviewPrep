/**
 Given a collection of distinct integers, return all possible permutations.
 * @param {number[]} nums
 * @return {number[][]}
 */

const permute = nums => {
    let ret = []

    const generate = (curr, remaining) => {
        curr = curr || []
        if(!remaining.length){
            ret.push(curr)
            return
        } else {
            //Move each index and permute
            for (let index = 0; index < remaining.length; index++){
                const currNum = remaining[index]
                generate(curr.concat(currNum), remaining.slice(0, index).concat(remaining.slice(index + 1)))
            }
        }
    }

    generate([], nums)
    return ret
}
