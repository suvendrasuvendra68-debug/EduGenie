async function sendRequest(mode) {
  let prompt = document.querySelector("textarea").value;
  let box = document.getElementById("response");
  if (!box) box = document.querySelector("div");
  box.innerHTML = "Thinking...";
  let res = await fetch("/ask", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({question: prompt, prompt: prompt, mode: mode})
  });
  let data = await res.json();
  console.log(data);
  box.innerHTML = data.answer || data.response || data.result || JSON.stringify(data);
}