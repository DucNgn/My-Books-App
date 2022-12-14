import { IUserProfile, IBookInfo, IShelvesStorage } from '@/interfaces';
import { MainState, AppNotification} from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';


export const mutations = {
    setToken(state: MainState, payload: string) {
        state.token = payload;
    },
    setLoggedIn(state: MainState, payload: boolean) {
        state.isLoggedIn = payload;
    },
    setLogInError(state: MainState, payload: boolean) {
        state.logInError = payload;
    },
    setUserProfile(state: MainState, payload: IUserProfile) {
        state.userProfile = payload;
    },
    setDashboardMiniDrawer(state: MainState, payload: boolean) {
        state.dashboardMiniDrawer = payload;
    },
    setDashboardShowDrawer(state: MainState, payload: boolean) {
        state.dashboardShowDrawer = payload;
    },
    addNotification(state: MainState, payload: AppNotification) {
        state.notifications.push(payload);
    },
    removeNotification(state: MainState, payload: AppNotification) {
        state.notifications = state.notifications.filter((notification) => notification !== payload);
    },
    setCurrentBook(state: MainState, payload: IBookInfo) {
        state.currentBook = payload;
    },
    setPersonalShelves(state: MainState, payload: IShelvesStorage) {
        state.personalShelves = payload;
    },
    setIsShowingAddBookDialog(state: MainState, payload: boolean) {
        state.isShowingAddBookDialog = payload;
    },
    setBookSearchResults(state: MainState, payload: IBookInfo[]) {
        state.bookSearchResults = payload;
    },
    removeBookSearchResults(state: MainState) {
        state.bookSearchResults = [];
    },
};

const {commit} = getStoreAccessors<MainState | any, State>('');

export const commitSetDashboardMiniDrawer = commit(mutations.setDashboardMiniDrawer);
export const commitSetDashboardShowDrawer = commit(mutations.setDashboardShowDrawer);
export const commitSetLoggedIn = commit(mutations.setLoggedIn);
export const commitSetLogInError = commit(mutations.setLogInError);
export const commitSetToken = commit(mutations.setToken);
export const commitSetUserProfile = commit(mutations.setUserProfile);
export const commitAddNotification = commit(mutations.addNotification);
export const commitRemoveNotification = commit(mutations.removeNotification);
export const commitChangeCurrentBook = commit(mutations.setCurrentBook);
export const commitSetShelves = commit(mutations.setPersonalShelves);
export const commitIsShowingAddBookDialog = commit(mutations.setIsShowingAddBookDialog);
export const commitSetBookSearchResults = commit(mutations.setBookSearchResults);
export const commitRemoveBookSearchResults = commit(mutations.removeBookSearchResults);

