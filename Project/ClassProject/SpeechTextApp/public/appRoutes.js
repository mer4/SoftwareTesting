angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'login',
        url: '/',
        templateUrl: 'public/components/templates/login.template.html',
        controller: 'LoginController'
    });

    $urlRouterProvider.otherwise('/');
}]);