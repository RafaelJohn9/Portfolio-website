let isLoggedIn = false;

function changeLoginStatus() {
    return {
        getLoginStatus: function() {
            return isLoggedIn;
        },
        setLoginStatus: function(status) {
            isLoggedIn = status;
        }
    };
}

module.exports = changeLoginStatus;