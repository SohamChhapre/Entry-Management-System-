import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
// import App from './App';
import * as serviceWorker from './serviceWorker';
import {BrowserRouter,Route,Link,withRouter} from 'react-router-dom'
import Home from './components/Home/index.jsx'
import VisitorForm from './components/vistorform';
import HostForm from './components/Hostform';
class App extends React.Component{
    constructor(){
        super();
        this.state={
            User:null
        };
    }
    // componentDidMount(){
    //     const user=localStorage.getItem('user');
        
    //     if (user){
    //         this.setState({
    //             User:JSON.parse(user)
    //         })
    //     }

    // }
    // setUser=(user)=>{
    //     this.setState({
    //         User:user
    //     });
    // }
    // removeauthuser=()=>{
    //     localStorage.removeItem('user');
    //     this.props.notyService.success('Successfully logged out!');
    //     this.setState({
    //         User:null
    //     })
    // }
   render(){
       
    return (
        <div>
        <Route exact path="/" component={ Home } />
        <Route exact path="/visitor"  render={ (props)=> <VisitorForm {...props} />} />
        <Route exact path="/host"  render={ (props)=> <HostForm {...props} />} />

    {/* { location.pathname!=='/login' && location.pathname!=='/signup' && <Navbar authUser={this.state.User} removeauthuser={this.removeauthuser} /> }
 
    
    <Route path='/signup' render={(props) => <Signup {...props} setUser={this.setUser} /> } />
    <Route path="/login" render={(props)=> <Login {...props} setUser={this.setUser} notyService={this.props.notyService}/>} />
    <Route exact path="/article/:id" render={(props)=> <SingleArticle {...props} getSingleArticle={this.props.articlesService.getSingleArticle}/>} />
    {this.state.User && <Route path='/articles/create' render={ (props)=> <CreateArticle {...props} user={this.state.User} /> } />}
    <Route exact path="user/article/:id" render={(props)=> <SingleArticle {...props} getSingleArticle={this.props.articlesService.getSingleArticle}/>} />
    <Route exact path='/community' Component={Welcome} />
    <Route exact path='/user/articles' render={ (props)=><UserArticles {...props} user={ this.state.User.data.name} getUserArticles={this.props.articlesService.getUserArticles} deleteArticle={this.props.articlesService.deleteArticle}/>}/> 
    { location.pathname!=='/login'  && location.pathname!=='/signup' && <Footer /> } */}
    </div>

    )
   }
}

const Main=withRouter((props )=>{
    return (
        <App {...props}   />
    )
    
});
ReactDOM.render(<BrowserRouter><Main /> </BrowserRouter>, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
