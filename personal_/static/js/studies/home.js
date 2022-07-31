ss={S1:[
  "Writings Paragraph",
  "Spoken English",
  "Study Skills",
  "Grammar 1",
  "Guided Reading",
  "Langues I ANG",
  "Reading Compr Précis 1"],S2:[
  "Reading Compr Précis 2",
  "Grammar 2",
  "Readings in Culture",
  "Langues II",
  "Composition 1",
  "Oral communication",
  "Business Communication",
]}

links = {S1:[
  "./s1/writing",
  "./s1/spoken",
  "./s1/study",
  "./s1/grammar1",
  "./s1/guided",
  "./s1/lang1",
  "./s1/reading1"],
  S2:[
  "./s2/reading2",
  "./s2/grammar2",
  "./s2/culture",
  "./s2/lang2",
  "./s2/comp1",
  "./s2/communication",
  "./s2/business",
]}


const semester=$('select[name=semester]')
let sselected = semester.val()
let sarr=ss[sselected]
let larr=links[sselected]
console.log(sarr)

$('.goto').attr('href', larr[0])
sarr.map((v, i) => {
  $(".gotoselect").append(`<option value=${larr[i]}>${v}</option>`);
});

semester.on('change', ()=>{
  $(".gotoselect").html('')
  $('.goto').attr('href', '#')
  let sselected = semester.val()
  let sarr=ss[sselected]
  let larr=links[sselected]
  console.log(sarr)

  $('.goto').attr('href', larr[0])
  sarr.map((v, i) => {
    $(".gotoselect").append(`<option value=${larr[i]}>${v}</option>`);
  });
})
$('.gotoselect').on('change', (e) => {
  v = e.target.value
  $('.goto').attr('href', v)
})