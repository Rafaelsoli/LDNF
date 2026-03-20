import { defineStore } from "pinia";
import axios from "axios";

export const useUserStore = defineStore(`user`, {

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null as string | null, // Tipagem para UUID
            nome: null as string | null,
            email: null as string | null,
            access: null as string | null,
            refresh: null as string | null,
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.nome = localStorage.getItem('user.nome')
                this.user.email = localStorage.getItem('user.email')
                this.user.isAuthenticated = true
                
                this.refreshToken()

                console.log('User inicializado do localStorage')
            }
        },
        setToken(data: any) {
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true
            
            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)
        },

        removeToken() {
            this.user.access = null
            this.user.refresh = null
            this.user.isAuthenticated = false
            localStorage.clear()
        },

        setUserInfo(user: any){
            console.log('SetUserInfo', user)
            this.user.id = user.id
            this.user.nome = user.nome
            this.user.email = user.email
            //! força a ignorar o risco de null
            localStorage.setItem('user.id', this.user.id!)
            localStorage.setItem('user.nome', this.user.nome!)
            localStorage.setItem('user.email', this.user.email!)

            console.log('user', this.user)
        },

        refreshToken(){
            console.log('Refreshing token...')
            axios.post('/api/token/refresh', {
                refresh: this.user.refresh
            })
                .then((response) =>{
                    this.user.access = response.data.access
                    localStorage.setItem('user.access', response.data.access)
                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error) => {
                    console.log(error)
                    this.removeToken()
                })
        },
    }
})