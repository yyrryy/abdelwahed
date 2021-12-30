const modals=[
    {
        h:"Polite request with 'I' as the subject",
        e:"May I, Could I, Can I(informal)"
    },
    {
        h:"Polite request with 'You' as the subject",
        e:"May I, Could I, Can I(informal)"
    },
    
]
const holder=$('.modals')

modals.map((mo, id)=>{
    holder.append(`
    <div class="tab border rounded">
        <input hidden type="checkbox" id="${id}">
        <label class="tab-label" for="${id}">${mo.h}</label>
        <div class="tab-content">
            ${mo.e}
        </div>
    </div>
    `)
})