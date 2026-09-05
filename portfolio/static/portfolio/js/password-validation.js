document.addEventListener("DOMContentLoaded", function () {

    const passwordField = document.querySelector(
        'input[name="password1"]'
    );

    const confirmPasswordField = document.querySelector(
        'input[name="password2"]'
    );

    if (!passwordField) {
        return;
    }


    /*
     * ---------------------------------------------------------
     * CREATE VALIDATION UI
     * ---------------------------------------------------------
     */

    const validationBox = document.createElement("div");

    validationBox.className = "password-validation";

    validationBox.innerHTML = `
        <div class="password-strength">
            <div class="password-strength-label">
                <span>Password strength</span>
                <span class="strength-text">Too weak</span>
            </div>

            <div class="strength-bar">
                <div class="strength-progress"></div>
            </div>
        </div>

        <div class="password-requirements">

            <div class="password-requirement" data-rule="length">
                <span class="requirement-icon">○</span>
                <span>At least 8 characters</span>
            </div>

            <div class="password-requirement" data-rule="letter">
                <span class="requirement-icon">○</span>
                <span>Contains a letter</span>
            </div>

            <div class="password-requirement" data-rule="number">
                <span class="requirement-icon">○</span>
                <span>Contains a number</span>
            </div>

            <div class="password-requirement" data-rule="numeric">
                <span class="requirement-icon">○</span>
                <span>Not entirely numeric</span>
            </div>

        </div>
    `;

    passwordField.insertAdjacentElement(
        "afterend",
        validationBox
    );


    /*
     * ---------------------------------------------------------
     * CONFIRM PASSWORD UI
     * ---------------------------------------------------------
     */

    let matchMessage = null;

    if (confirmPasswordField) {

        matchMessage = document.createElement("div");

        matchMessage.className = "password-match-message";

        confirmPasswordField.insertAdjacentElement(
            "afterend",
            matchMessage
        );
    }


    /*
     * ---------------------------------------------------------
     * UPDATE REQUIREMENT
     * ---------------------------------------------------------
     */

    function updateRequirement(rule, valid) {

        const requirement = validationBox.querySelector(
            `[data-rule="${rule}"]`
        );

        if (!requirement) {
            return;
        }

        const icon = requirement.querySelector(
            ".requirement-icon"
        );

        if (valid) {

            requirement.classList.add("valid");

            icon.textContent = "✓";

        } else {

            requirement.classList.remove("valid");

            icon.textContent = "○";
        }
    }


    /*
     * ---------------------------------------------------------
     * PASSWORD VALIDATION
     * ---------------------------------------------------------
     */

    function validatePassword() {

        const password = passwordField.value;

        const hasLength = password.length >= 8;

        const hasLetter = /[A-Za-z]/.test(password);

        const hasNumber = /[0-9]/.test(password);

        const notEntirelyNumeric =
            password.length > 0 &&
            !/^[0-9]+$/.test(password);


        updateRequirement(
            "length",
            hasLength
        );

        updateRequirement(
            "letter",
            hasLetter
        );

        updateRequirement(
            "number",
            hasNumber
        );

        updateRequirement(
            "numeric",
            notEntirelyNumeric
        );


        /*
         * -----------------------------------------------------
         * PASSWORD STRENGTH
         * -----------------------------------------------------
         */

        let score = 0;

        if (hasLength) {
            score++;
        }

        if (hasLetter) {
            score++;
        }

        if (hasNumber) {
            score++;
        }

        if (notEntirelyNumeric) {
            score++;
        }


        /*
         * Additional strength indicators
         */

        if (password.length >= 12) {
            score++;
        }

        if (/[^A-Za-z0-9]/.test(password)) {
            score++;
        }


        const strengthProgress =
            validationBox.querySelector(
                ".strength-progress"
            );

        const strengthText =
            validationBox.querySelector(
                ".strength-text"
            );


        let percentage = 0;
        let text = "Too weak";


        if (password.length === 0) {

            percentage = 0;
            text = "Too weak";

        } else if (score <= 2) {

            percentage = 35;
            text = "Weak";

        } else if (score <= 4) {

            percentage = 65;
            text = "Moderate";

        } else {

            percentage = 100;
            text = "Strong";
        }


        strengthProgress.style.width =
            percentage + "%";

        strengthText.textContent = text;


        validationBox.classList.remove(
            "strength-weak",
            "strength-moderate",
            "strength-strong"
        );


        if (score <= 2) {

            validationBox.classList.add(
                "strength-weak"
            );

        } else if (score <= 4) {

            validationBox.classList.add(
                "strength-moderate"
            );

        } else {

            validationBox.classList.add(
                "strength-strong"
            );
        }


        validatePasswordMatch();
    }


    /*
     * ---------------------------------------------------------
     * PASSWORD MATCH
     * ---------------------------------------------------------
     */

    function validatePasswordMatch() {

        if (!confirmPasswordField || !matchMessage) {
            return;
        }

        const password =
            passwordField.value;

        const confirmation =
            confirmPasswordField.value;


        if (confirmation.length === 0) {

            matchMessage.textContent = "";

            matchMessage.className =
                "password-match-message";

            return;
        }


        if (password === confirmation) {

            matchMessage.innerHTML =
                "✓ Passwords match";

            matchMessage.className =
                "password-match-message valid";

        } else {

            matchMessage.innerHTML =
                "✕ Passwords do not match";

            matchMessage.className =
                "password-match-message invalid";
        }
    }


    /*
     * ---------------------------------------------------------
     * LIVE VALIDATION
     * ---------------------------------------------------------
     */

    passwordField.addEventListener(
        "input",
        validatePassword
    );


    if (confirmPasswordField) {

        confirmPasswordField.addEventListener(
            "input",
            validatePasswordMatch
        );
    }


    /*
     * Initial validation
     */

    validatePassword();

});