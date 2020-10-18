function checkTask(task_number=0, hash=true) {

    let x = 5;

    let answer = Math.log(Math.abs(12 * Math.sin(x)));
    let begin = new Date().getTime();
    let userAnswer = prompt(`x = ${x} \nЧему равно log10(abs(12*sin(x)))?\nРешите задачу за 3 сек, чтобы получить скидку.\nПри успешном решении вы найдете проверочный код в консоли браузера.`);
    let end = new Date().getTime();
    let distance = end - begin;
    if (Math.abs(userAnswer - answer) <= 1e-13 && distance <= 3000) {
        if (hash) {
            let hashcode = getHashcode(task_number);
            alert(`Поздравляем, вы справились! Вставьте это число в поле ответа на Stepik: ${hashcode}`);
            console.log(`Поздравляем, вы справились! Вставьте это число в поле ответа на Stepik: ${hashcode}`);
        }
        return true;
    }
    alert("Неверный ответ или закончилось время! Попробуйте запустить тест снова.");
    return false;
}


