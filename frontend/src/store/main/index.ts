import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { MainState } from './state';

const defaultState: MainState = {
  isLoggedIn: null,
  token: '',
  logInError: false,
  userProfile: null,
  dashboardMiniDrawer: false,
  dashboardShowDrawer: true,
  notifications: [],
  currentBook: null,
  personalShelves: null,
  isShowingAddBookDialog: false,
  bookSearchResults: [],
};

export const mainModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
