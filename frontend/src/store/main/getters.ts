import { MainState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
  hasAdminAccess: (state: MainState) => {
    return (
      state.userProfile &&
      state.userProfile.is_superuser &&
      state.userProfile.is_active
    );
  },
  loginError: (state: MainState) => state.logInError,
  dashboardShowDrawer: (state: MainState) => state.dashboardShowDrawer,
  dashboardMiniDrawer: (state: MainState) => state.dashboardMiniDrawer,
  userProfile: (state: MainState) => state.userProfile,
  token: (state: MainState) => state.token,
  isLoggedIn: (state: MainState) => state.isLoggedIn,
  firstNotification: (state: MainState) =>
    state.notifications.length > 0 && state.notifications[0],
  currentBook: (state: MainState) => state.currentBook,
  personalShelves: (state: MainState) => state.personalShelves,
  isShowingAddBookDialog: (state: MainState) => state.isShowingAddBookDialog,
  bookSearchResults: (state: MainState) => state.bookSearchResults,
};

const { read } = getStoreAccessors<MainState, State>('');

export const readDashboardMiniDrawer = read(getters.dashboardMiniDrawer);
export const readDashboardShowDrawer = read(getters.dashboardShowDrawer);
export const readHasAdminAccess = read(getters.hasAdminAccess);
export const readIsLoggedIn = read(getters.isLoggedIn);
export const readLoginError = read(getters.loginError);
export const readToken = read(getters.token);
export const readUserProfile = read(getters.userProfile);
export const readFirstNotification = read(getters.firstNotification);
export const readCurrentBookInfo = read(getters.currentBook);
export const readPersonalShelves = read(getters.personalShelves);
export const readShowAddBookDialog = read(getters.isShowingAddBookDialog);
export const readBookSearchResults = read(getters.bookSearchResults);
