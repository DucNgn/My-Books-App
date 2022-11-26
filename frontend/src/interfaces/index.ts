export interface IUserProfile {
    favorite_genres: string[];
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}


export interface IShelvesStorage {
    id: string;
    reading_shelf: IBookInfo[];
    toread_shelf: IBookInfo[];
    read_shelf: IBookInfo[];
    favorite_shelf: IBookInfo[];
    recommendation_shelf: IBookInfo[];
}

export interface IBookInfo {
    id: string;
    title: string;
    author: string;
    rating: string;
    description: string;
    isbn: string;
    genre: string;
    num_of_pages: number;
    publisher: string;
    publication_year: string;
    cover_image_url: string;
}
