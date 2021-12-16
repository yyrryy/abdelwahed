let termsholder=$('.terms')
let searchinp=$('.search')

let terms=[
    {
        t:'Allegory',
        d:'<p>A literary work in which nearly all of the characters, events, settings, and other literal elements ofthe story have a second, symbolic meaning. In most cases, allegories advance a very clear moral lesson.</p><p><em>George Orwell’s</em>Animal Farm <em>is an <strong>allegory</strong> in which the barnyard animals who overthrow the farmer and take over the farm represent the Russian Revolution and its  aftermath.</em> </p>'
    },
    {
        t:'Alletiration',
        d:'<p>The repetition of an initial consonant sound in words that are close together, such as within a single sentence or line of poetry.</p> <p> <em>The third stanza of Emily Dickinson’s</em>“A narrow Fellow in the Grass” <em>uses <strong>alliteration</strong> in both the second and third lines:</em> </p> <p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;line-height:normal;"> <em>He likes a Boggy Acre - </em></p> <p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;line-height:normal;"> <em>A  Floor too <u>c</u>ool for <u>C</u>orn -</em></p>  <p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;line-height:normal;"> <em><u>B</u>ut when a <u>B</u>oy and <u>B</u>arefoot</em> </p> <p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:.5in;line-height:normal;"> <em>I more than once at Noon</em></p>'
    }

]


const display= (ls)=>{
    let el=ls.map((l, i)=>{
        
        return `
        <div class="col-md-6 tabs mb-3">
            <div class="tab">
                <input hidden type="checkbox" id="chck${i}">
                <label class="tab-label" for="chck${i}">${l.t}</label>
                <div class="tab-content">
                    ${l.d}
                </div>
            </div>
        </div>
        `
    }).join('')
    termsholder.html(el)
}







display(terms)

searchinp.on('input', (e)=>{
    tar=searchinp.val()
    let filtered= tar?terms.filter(term=>{
        return term.t.toLowerCase().includes(tar)
    }):terms
    display(filtered)
})