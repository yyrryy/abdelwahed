let stories=[
    {
        title: 'The lottary',
        themes: ['theme1', 'theme2'],
        summary: 'summ',
        chracters: ['char1', 'char2']
    },
    {
        title: 'The lady with the pet dog',
        themes: ['theme1', 'theme2'],
        summary: 'summary',
        chracters: ['char1', 'char2']
    },
    {
        title: 'The tale tale heart',
        themes: ['theme1', 'theme2'],
        summary: 'summary tale',
        chracters: ['char1', 'char2']
    },
    {
        title: 'The biss',
        themes: ['theme1', 'theme2'],
        summary: 'summary bl',
        chracters: ['char1', 'char2']
    },
    {
        title: 'The necklace',
        themes: ['theme1', 'theme2'],
        summary: 'summary',
        chracters: ['char1', 'char2']
    },
    {
        title: 'The Blue stones',
        themes: ['theme1', 'theme2'],
        summary: 'The story The Blue Stones is short and it seems simple. The skipper named his ship after his wife, "He had the figurehead of it beautifully carved, just like her, and the hair of it gilt". His wife was jealous about his passion, she even thought that he liked the ship more than her. During one adventure he helped the king of savages and he was bestowed by the two precious blue stones. As such, it seemed as if his ship had found eyes. The wife was jealous about these stones so much that she secretly replaced them with false stones and kept the original ones at home.Soon after that, the wife found that her eyesight was growing worse, and she could not see to thread a needle. She was going blind; she cried, "I should have the glass taken out, and the jewels put back." She wanted to do it but it was not possible. This sailing was last for her husband. She got a letter from the Consul of Portugal, that the ship had wrecked, "And it was a very strange thing, the Consul wrote, that in broad daylight she had run straight into a tall rock, rising out of the sea."',
        chracters: ['char1', 'char2']
    },
    
]


let shortsholder=$('.shorts')
let searchinp=$('.search')




const display= (ls)=>{
    let el=ls.map((l, i)=>{
        id=l.title.split(' ')[1]
        return `
        <div class="story mb-5 border">
        <h1 class="mt-3 text-center title">
          ${l.title}
        </h1>
        <div class="tabs">
          <div class="tab">
            <input hidden type="checkbox" id="chck${i+1}${id}">
            <label class="tab-label" for="chck${i+1}${id}">Summary</label>
            <div class="tab-content">
              ${l.summary}
            </div>
          </div>
          <div class="tab">
            <input hidden type="checkbox" id="chck${i+2}${id}">
            <label class="tab-label" for="chck${i+2}${id}">Themes</label>
            <div class="tab-content">
              ${l.themes.join('<br>')}
            </div>
          </div>
          <div class="tab">
            <input hidden type="checkbox" id="chck${i+3}${id}">
            <label class="tab-label" for="chck${i+3}${id}">Chracters</label>
            <div class="tab-content">
              ${l.chracters.join('<br>')}
            </div>
          </div>
        </div>
    
      </div>
        `
    }).join('')
    shortsholder.html(el)
}







display(stories)

searchinp.on('input', (e)=>{
    tar=searchinp.val()
    let filtered= tar?stories.filter(story=>{
        return story.title.toLowerCase().includes(tar)
    }):stories
    display(filtered)
})