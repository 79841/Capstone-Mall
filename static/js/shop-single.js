// console.log("111111111111111111111111111111111111");
relatedProductNames = document.getElementsByClassName("related-product-name");
// console.log(relatedProductNames);
window.onload = function () {
  for (rpn of relatedProductNames) {
    if (rpn.innerText.length > 10) {
      rpn.innerText = `${rpn.innerText.slice(0, 14)}...`;
    }
  }
};
